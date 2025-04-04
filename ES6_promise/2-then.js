function handleResponseFromAPI(promise) {
  return promise
    .then(() => {
      const result = { status: 200, body: 'Success' };
      return result;
    })
    .catch(() => {
      const error = new Error();
      return error;
    })
    .finally(() => {
      console.log('Got a response from the API');
    });
}

export default handleResponseFromAPI;
