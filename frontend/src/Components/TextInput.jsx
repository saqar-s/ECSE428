import React from "react";
import { FormControl, FormLabel, TextField } from "@mui/material";
import { COLORS, FONTS } from "../GLOBAL";

const TextInput = ({
  label,
  text,
  helpertext,
  hasError,
  isMultiline,
  onClick,
  style,
  width = "50%",
}) => {
  return (
    <FormControl sx={{ width: width, ...style }}>
      <FormLabel
        sx={{
          color: COLORS.Black,
          fontFamily: FONTS.InriaSerif,
          fontSize: 16,
          marginBottom: 0.5,
        }}
      >
        {label}
      </FormLabel>
      <TextField
        id="outlined-basic"
        InputProps={{
          style: {
            color: COLORS.Black,
            border: "none",
            borderRadius: 16,
            backgroundColor: COLORS.White,
            height: "50px",
          },
        }}
        helperText={hasError ? helpertext : ""}
        multiline={isMultiline ? true : false}
        onChange={onClick()}
        value={text}
      ></TextField>
    </FormControl>
  );
};
export default TextInput;
