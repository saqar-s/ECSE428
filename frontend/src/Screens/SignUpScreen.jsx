import React from "react";
import {
  TitleText,
  SubTitleText,
  TextInput,
  CustomButton,
} from "../Components";
import { FONTS } from "../GLOBAL";
import { useNavigate } from "react-router-dom";

const SignUpScreen = () => {
  const [username, setUsername] = React.useState("");
  const [password, setPassword] = React.useState("");
  const [age, setAge] = React.useState("");
  const [name, setName] = React.useState("");
  const navigate = useNavigate();

  const handleUsernameChange = (text) => {
    setUsername(text);
  };

  const handlePasswordChange = (text) => {
    setPassword(text);
  };

  const handleNameChange = (text) => {
    setName(text);
  };

  const handleAgeChange = (text) => {
    setAge(text);
  };

  const handleLogIn = () => {
    //console.log("LogedIn");
    navigate("/signin");
  };

  const handleSignUp = () => {
    //console.log("Sign Up");
  };

  return (
    <div
      style={{
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        margin: 12,
      }}
    >
      <TitleText text={"Hello!"} />
      <div style={{ marginBottom: "10%" }}>
        <SubTitleText
          text={"Please Sign up or login to get the most out of our website"}
        />
      </div>

      <TextInput
        label={"Email (This will be your username)"}
        text={username}
        onClick={handleUsernameChange}
        style={{ marginBottom: 6 }}
      />
      <TextInput
        label={"Password"}
        text={password}
        onClick={handlePasswordChange}
        style={{ marginBottom: 6 }}
      />

      <TextInput
        label={"Name"}
        text={name}
        onClick={handleNameChange}
        style={{ marginBottom: 6 }}
      />
      <TextInput
        label={"Age"}
        text={age}
        onClick={handleAgeChange}
        style={{ marginBottom: 6 }}
      />

      <CustomButton
        label={"Sign Up"}
        onClick={handleSignUp}
        style={{ width: "10%", height: "40px", marginBottom: 6 }}
      />
      <div style={{ fontFamily: FONTS.InriaSerif, fontSize: 16 }}>
        Already have an account
      </div>
      <CustomButton
        label={"Log In"}
        onClick={handleLogIn}
        style={{ width: "10%", height: "40px", marginTop: 1, marginBottom: 5 }}
      />
    </div>
  );
};

export default SignUpScreen;
