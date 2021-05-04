import React from "react";
import GitHubLogin from "react-github-login";
import axios from "axios";

//GitHub login button from GitHub's OAuth tutorial
//Updates bookmarks on login. Stores token to localStorage.

const GithubLoginButton = ({bookmarkUpdater}) => {
  const onSuccess = response => {
    console.log(response);
	alert(JSON.stringify(response));
	sendGithubAuthCode(response);
	bookmarkUpdater();

  };
  const onFailure = response => console.error(response);
  return (
    <GitHubLogin
      clientId="0e04fc00c07db82338b0"
      onSuccess={onSuccess}
      onFailure={onFailure}
      redirectUri=""
      buttonText="Login with Github"
      className="fa fa-github btn btn-primary"
    />
  );
};

const url = "http://localhost:8000";


const sendGithubAuthCode = async (code) =>{
	
	const headers = {
          "Content-Type": "application/json",
          Accept: "application/json"
        }
		try{
			let response = await axios.post('/githubverify/', JSON.stringify(code), {headers: headers});
			console.log(response.data);
			if(response.data != null){
				console.log(response.data.token);
				localStorage.setItem('token',response.data.token);
			}
		}catch(err){
			
		}

}

export default GithubLoginButton;