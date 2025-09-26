async function generate() {
    let prompt=document.getElementById("prompt").value
    let chat_id="chat1"

    let res=await fetch("http://localhost:8000/generate",{
        method:"POST",
        headers:{"Content-Type":"application/json"},
        body:JSON.stringify({prompt,chat_id})
    })
    let data=await res.json()

    // update output
    document.getElementById("output").innerText=
        `Version ${data.version}\n\n${data.code}`

    // add version to dropdown
    let sel=document.getElementById("version")
    let opt=document.createElement("option")
    opt.value=data.version
    opt.text=`v${data.version}`
    sel.appendChild(opt)
}

async function selectVersion() {
    let chat_id="chat1"
    let v=document.getElementById("version").value
    if(!v) return
    let res=await fetch(`http://localhost:8000/history/${chat_id}/${v}`)
    let data=await res.json()
    document.getElementById("output").innerText=
        `Version ${v}\n\n${data.code}`
}
