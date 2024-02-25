import React from "react";
import { Button } from "@mui/material";
import { COLORS } from "../GLOBAL";

const CustomButton = ({ label, onClick, style }) => {
  return (
    <Button
      sx={{
        backgroundColor: COLORS.PrimaryPink,
        borderRadius: 12,
        border: "1px solid #000000",
        color: COLORS.Black,
        textTransform: "none",
        "&:hover": { background: COLORS.PrimaryPink },
        ...style,
      }}
      onClick={onClick}
    >
      {label}
    </Button>
  );
};
export default CustomButton;
