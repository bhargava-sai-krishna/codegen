import React, { useState } from "react";
import { marked } from "marked";
import hljs from "highlight.js";
import "highlight.js/styles/github-dark.css"; // check styles folder for others
import "./App.css";

marked.setOptions({
  highlight: function (code, lang) {
    const validLang = hljs.getLanguage(lang) ? lang : "plaintext";
    return hljs.highlight(code, { language: validLang }).value;
  },
});

export default function App() {
  const [prompt, setPrompt] = useState("");
  const [output, setOutput] = useState("");
  const [versions, setVersions] = useState([]);
  const [selectedVersion, setSelectedVersion] = useState("");

  async function generate() {
    const res = await fetch("http://localhost:8000/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt, chat_id: "default" }),
    });
    const data = await res.json();

    setOutput(marked.parse(data.code));
    setVersions((prev) => [...prev, { version: data.version, code: data.code }]);
    setSelectedVersion(data.version);
  }

  async function selectVersion(version) {
    const res = await fetch(`http://localhost:8000/history/default/${version}`);
    const data = await res.json();

    setOutput(marked.parse(data.code));
    setSelectedVersion(version);
  }

  return (
    <div className="container">
      <h1>Code Generator</h1>
      <textarea
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter your prompt"
      />
      <br />
      <button onClick={generate}>Generate</button>

      <h2>History</h2>
      <div>
        <label htmlFor="version">Select Version: </label>
        <select
          id="version"
          value={selectedVersion}
          onChange={(e) => selectVersion(e.target.value)}
        >
          <option value="">--</option>
          {versions.map((v) => (
            <option key={v.version} value={v.version}>
              Version {v.version}
            </option>
          ))}
        </select>
      </div>

      <div
        id="output"
        className="output"
        dangerouslySetInnerHTML={{ __html: output }}
      />
    </div>
  );
}
