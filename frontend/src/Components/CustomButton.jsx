import React from "react";
import { Button } from "@mui/material";
import { COLORS } from "../GLOBAL";

const CustomButton = ({ label, onClick, style , backgroundChangeColor = COLORS.PrimaryPink, backgroundColor = COLORS.PrimaryPink}) => {
  return (
    <Button
      sx={{
        backgroundColor: backgroundColor,
        borderRadius: 12,
        border: "1px solid #000000",
        color: COLORS.Black,
        textTransform: "none",
        "&:hover": { background: backgroundChangeColor },
        ...style,
      }}
      onClick={onClick}
    >
      {label}
    </Button>
  );
};
export default CustomButton;
