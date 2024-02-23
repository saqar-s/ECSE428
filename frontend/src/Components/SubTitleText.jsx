import React from "react";
import { FONTS } from "../GLOBAL";

const SubTitleText = ({ text, size = "2vw" }) => {
  return (
    <div style={{ fontFamily: FONTS.IrishGrover, fontSize: size }}>{text}</div>
  );
};

export default SubTitleText;
