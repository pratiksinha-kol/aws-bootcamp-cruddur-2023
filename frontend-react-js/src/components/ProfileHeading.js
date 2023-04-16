import './ProfileHeading.css';
import EditProfileButton from '../components/EditProfileButton';

export default function ProfileHeading(props) {
  const backgroundImages = 'url("https://assets.pratiksinha.link/banners/banner1.jpg")';
  const styles = {
    backgroundImages: backgroundImages,
    backgroundSize: 'cover',
    backgroundPosition: 'center',
  }
  return (
    <div className='activity_feed_heading profile_heading'>
          <div className='title'>{props.profile.display_name}</div>
          <div className="cruds_count">{props.profile.cruds_count}Cruds</div>
          <div className="banner" style={styles}>
            <div className='avatar'>
              <img src='https://assets.pratiksinha.link/avatars/data.jpg'></img>
            </div>
          </div>
          
          <div className='display_name'>{props.display_name}</div>
          <div className='handle'>{props.handle}</div>
          <EditProfileButton setPopped={props.setPopped}/>
    </div>
  );
}