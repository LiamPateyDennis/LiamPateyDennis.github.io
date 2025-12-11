import { createTheme } from "@mui/material/styles";

const theme = createTheme({
  components: {
    MuiTypography: {
      defaultProps: {
        variantMapping: {
          h1: "h2",
          h2: "h2",
          h3: "h2",
          h4: "h2",
          h5: "h2",
          h6: "h2",
          subtitle1: "h2",
          subtitle2: "h2",
          body1: "span",
          body2: "span",
        },
      },
    },
  },
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
    background: {
      paper: "#000000",
    },
    text: {
      primary: "#fff",
      secondary: "#eff9e9",
    },
  },
});

export default theme;
