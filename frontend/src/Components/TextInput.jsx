import React, { useState } from "react";
import {
  FormControl,
  FormLabel,
  TextField,
  InputAdornment,
  IconButton,
  Typography,
} from "@mui/material";
import { COLORS, FONTS } from "../GLOBAL";
import Visibility from "@mui/icons-material/Visibility";
import VisibilityOff from "@mui/icons-material/VisibilityOff";

const TextInput = ({
  label,
  text,
  helpertext,
  hasError,
  isMultiline,
  onClick,
  style,
  width = "50%",
  hide,
  labelColor = COLORS.Black,
  inputHeight = "50px"
}) => {
  const [showPassword, setShowPassword] = useState(false);

  const handleChange = (event) => {
    onClick(event.target.value);
  };

  const handleTogglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  return (
    <FormControl sx={{ width: width, ...style }}>
      <FormLabel
        sx={{
          color: labelColor,
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
            height: inputHeight,
          },
          endAdornment: hide && (
            <InputAdornment position="end">
              <IconButton onClick={handleTogglePasswordVisibility} edge="end">
                {showPassword ? <Visibility /> : <VisibilityOff />}
              </IconButton>
            </InputAdornment>
          ),
        }}
        type={hide && !showPassword ? "password" : "text"}
        helperText={
          hasError ? (
            <Typography variant="caption" sx={{ color: "red" }}>
              {helpertext}
            </Typography>
          ) : (
            ""
          )
        }
        multiline={isMultiline ? true : false}
        onChange={handleChange}
        value={text}
      />
    </FormControl>
  );
};

export default TextInput;
