import React, { useEffect } from "react";
import {
  TitleText,
  SubTitleText,
  TextInput,
} from "../Components";
import { COLORS, FONTS } from "../GLOBAL";
import {getUserList} from "../APIcalls/AccountCalls";
const UserListScreen = () => {
  const [names, setNames] = React.useState([]);
  useEffect(() => {
    getNames();
  },[]);
  const getNames = async () => {
    const names = await getUserList();
    //console.log(names[0]);
    setNames(names);
  }
  return (
    <div style={{
      display: "flex",
      flexDirection: "column",
      alignItems: "center",
      margin: 12,
    }}>
        <TitleText text={"User List"} />
      <div style={{ marginBottom: "6%" }}>
        <SubTitleText text={"WOW look at all these users!"} />
      </div>
      <div>
        {names.map((name,index) => (
          <li key={index}>{name}</li>
        ))}
      </div>
    </div>
  );
};

export default UserListScreen;