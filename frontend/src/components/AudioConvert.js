import axios from 'axios';
import { useState } from 'react';


function AudioConvert() {

    const [file, setFile] = useState(null);

    const handleSubmit = (e)=>{
        e.preventDefault()
        if(file == null) {
            alert("파일을 업로드 해주세요")
            return
        }
        const form = new FormData();
        form.append('file', file)

        axios.post('http://localhost:8000/convert/audio/upload', form, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }}).then(res=>{
                document.getElementById("result_original").innerHTML = res.data.original_text
                document.getElementById("result_summary").innerHTML = res.data.summary_text
            
            })
    }

    return (
    <div>
        <h3>오디오 파일을 업로드 해 주세요</h3>
        <hr />
        <form>
            <input type = "file" name = "file" onChange={(e)=>setFile(e.target.files[0])}/>< br/>
            <input type = "submit" onClick={e=>handleSubmit(e)}/>
        </form>
        <br /><br />
        <h3>원문</h3>
        <p id="result_original"></p>

        <h3>요약본</h3>
        <p id="result_summary"></p>
    </div>
    );

    
  }
  


  export default AudioConvert;