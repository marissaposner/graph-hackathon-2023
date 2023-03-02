import styled from "@emotion/styled";
import { Select } from "@mui/material";

export const StyledSelect = styled(Select)`
  height: 45px;
  width: 100%;
  color: white;
  & .MuiOutlinedInput-notchedOutline {
    border-color: white
  };
  &.Mui-focused .MuiOutlinedInput-notchedOutline {
    border-color: white
  };
  &:hover .MuiOutlinedInput-notchedOutline {
    border-color: white;
    border-width: 2px
  };
  // & > fieldset {
  //   border-color: white;
  // };
  & > svg {
    color: white;
  }
  `;