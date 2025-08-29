import { uploadPhoto, createUser } from './utils.js';

export default async function handleProfileSignup() {
  const newPromise = Promise.all([uploadPhoto(), createUser()]);
  try {
        const [photoBody, userFullName] = await newPromise;
        console.log(`${photoBody.body} ${userFullName.firstName} ${userFullName.lastName}`);
    } catch {
        console.log('Signup system offline');
    }
}
