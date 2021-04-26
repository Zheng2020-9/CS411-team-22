import React from "react";
import GitHubLogin from "react-github-login";
import axios from "axios";


const GithubLoginButton = props => {
  const onSuccess = response => {
    console.log(response);
	alert(JSON.stringify(response));
    //sendGithubCode(response);
	testSendGithubAuthCode(response);
  };
  const onFailure = response => console.error(response);
  return (
    <GitHubLogin
      clientId="ce1bfb1626bb04675b10"
      onSuccess={onSuccess}
      onFailure={onFailure}
      redirectUri=""
      buttonText="Login with Github"
      className="fa fa-github btn btn-primary"
    />
  );
};

const url = "http://localhost:8000";

const isSendingGithubCode = () => ({
  type: "SENDING_GITHUB_CODE"
});

function sentGithubCodeSuccess(json) {
  localStorage.setItem("github_access_token_conv", json.token.access_token);
  localStorage.setItem(
    "github_name",
    json.user.first_name + " " + json.user.last_name
  );
  localStorage.setItem("github_email", json.user.email);
  return {
    type: "SENT_GITHUB_CODE_SUCCESS",
    token_user_obj: json
  };
}


function githubLogoutAction() {
  return function(dispatch) {
    localStorage.removeItem("github_access_token_conv");
    localStorage.removeItem("github_name");
    localStorage.removeItem("github_email");
    dispatch({ type: "GITHUB_LOGOUT" });
    return Promise.resolve();
  };
}

const sentGithubCodeFailure = err => ({
  type: "SENT_GITHUB_CODE_FAILURE",
  err
});

function testSendGithubAuthCode(code){
	
	const headers = {
          "Content-Type": "application/json",
          Accept: "application/json"
        }
		
		axios.post('/githubverify/', JSON.stringify(code), {headers: headers});

}

function sendGithubCode(code) {
  return async function(dispatch) {
    dispatch(isSendingGithubCode());
    try {
      let response = await fetch('localhost:8000/githubverify/', {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Accept: "application/json"
        },
        body: JSON.stringify(code)
      });
      if (!response.ok) {
        throw new Error("Invalid authorization with Github. Please try again.");
      }
      let responseJson = await response.json();
      return dispatch(sentGithubCodeSuccess(responseJson));
    } catch (err) {
      return dispatch(sentGithubCodeFailure(err));
    }
  };
}

export default GithubLoginButton;