import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  palette: {
    primary: {
      light: "#767676",
      main: "#000000",
      dark: "#000000",
      contrastText: "#fff",
    },
    secondary: {
      light: "#4acc41",
      main: "#4acc41",
      dark: "#00700f",
      contrastText: "#eff9e9",
    },
  },
});

export default theme;
