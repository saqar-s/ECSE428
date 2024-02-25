import React from "react";
import { FONTS } from "../GLOBAL";

const TitleText = ({ text, size = "4vw" }) => {
  return (
    <div style={{ fontFamily: FONTS.IrishGrover, fontSize: size }}>{text}</div>
  );
};

export default TitleText;
