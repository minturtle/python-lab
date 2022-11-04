import {Link} from 'react-router-dom';


function Header() {
    return (
    <div>
        <Link to="/audio/convert">
            <input type="button" value="mp3 텍스트 변환& 요약"/>
        </Link>
    </div>
    );
  }
  
  export default Header;