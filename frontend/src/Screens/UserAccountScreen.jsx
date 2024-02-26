import React from "react";
import {
  TitleText,
  SubTitleText,
  TextInput,
  CustomButton,
} from "../Components";

import { useLocation } from "react-router-dom";
import { modifyUserDetails } from "../APIcalls/AccountCalls";
import { logoutUser } from "../APIcalls/AccountCalls";
import { useNavigate } from "react-router-dom";


const UserAccountScreen = () => {
  const location = useLocation();
  const navigate = useNavigate();
  const { username, name, age, password } = location.state;

  const [usernameModified, setUsername] = React.useState(username);
  const [ageModified, setAge] = React.useState(age);
  const [nameModified, setName] = React.useState(name);
  const [passwordModified, setPassword] = React.useState(password);

  const handleUsernameChange = (text) => {
    setUsername(text);
  };

  const handleNameChange = (text) => {
    setName(text);
  };

  const handleAgeChange = (text) => {
    setAge(text);
  };

  const handlePasswordChange = (text) => {
    setPassword(text);
  };

  const handleModify = async () => {
    try{
      const response = await modifyUserDetails({name: nameModified, age: ageModified, email: username});
      console.log(response);
      console.log("Changing info to: ", nameModified, ageModified)
      console.log("From: ", name,  age);
    }
    catch (error) {
      console.error("Could not modify data: ", error)
    }
  };

  const handleLogout = async () => {
    try {
      const response = await logoutUser();
      console.log(response);
    }catch (error){
      console.error("Could not logout: ", error);
    }
    navigate("/signin");
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
      <TitleText text={`Hello ${name}!`} />
      <div style={{ marginBottom: "6%" }}>
        <SubTitleText
          text={"Welcome to your account.You can modify or delete your account"}
        />
      </div>

      <span style={{ color: 'red' }}> *You cannot modify your email</span>
      <TextInput
        label={"Username"}
        text={usernameModified}
        onClick={handleUsernameChange}
        style={{ marginBottom: 6 }}
      />
      <TextInput
        label={"Name"}
        text={nameModified}
        onClick={handleNameChange}
        style={{ marginBottom: 6 }}
      />
      <TextInput
        label={"Age"}
        text={ageModified}
        onClick={handleAgeChange}
        style={{ marginBottom: 6 }}
      />
      <div
        style={{
          display: "flex",
          flex: 1,
          flexDirection: "row",
          gap: "10%",
          width: "100%",
          justifyContent: "center",
        }}
      >
        <CustomButton 
          label={"Save"} 
          style={{ width: "10%", height: "40px" }} 
          onClick={handleModify} />
        <CustomButton
          label={"Delete Account"}
          style={{ width: "10%", height: "40px" }}
        />
        <CustomButton
          label={"Log out"}
          style={{ width: "10%", height: "40px" }}
          onClick={handleLogout}
        />
      </div>
    </div>
  );
};
export default UserAccountScreen;