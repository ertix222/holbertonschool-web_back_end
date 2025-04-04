import { uploadPhoto, createUser } from './utils';

function handleProfileSignup() {
  return Promise.all([uploadPhoto(), createUser()])
    .then(([photo, user]) => {
      const result = `${photo.body} ${user.firstName} ${user.lastName}`;
      console.log(result);
    })
    .catch(() => {
      const error = 'Signup system offline';
      console.log(error)
    });
}

export default handleProfileSignup;
