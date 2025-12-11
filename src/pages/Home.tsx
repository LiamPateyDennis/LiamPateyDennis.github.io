import Box from "@mui/material/Box";
import Container from "@mui/material/Container";
import { Typography } from "@mui/material";
import theme from "../types/theme";
import { ThemeProvider } from "@mui/material";
import { Grid } from "@mui/material";

function Home() {
  return (
    <ThemeProvider theme={theme}>
      <Grid
        display="flex"
        justifyContent="center"
        alignItems="center"
        size="grow"
      >
        <Box
          component="section"
          sx={{
            p: 3,
            typography: "body1",
            width: 800,
            borderRadius: 5,
            border: "1px dashed white",
            bgcolor: "primary.dark",
            mt: 5,
          }}
        >
          <Box></Box>
          <Box
            sx={{
              color: "primary.contrastText",
              fontSize: 15,
              fontWeight: 200,
              fontFamily: "monospace",
            }}
          >
            The quality of a message depends entirely on the strength of the
            signal received. In the early 1940s, Richard Hamming confronted this
            challenge while working at Bell Labs. There, he had access to the
            relay-based Bell Model V Computer, a machine used for complex
            engineering calculations that often ran unattended over weekends.
            Frustrated by the frequent errors it produced, Hamming set out to
            develop a method that could not only detect mistakes but also
            automatically correct them.
          </Box>
        </Box>
      </Grid>
    </ThemeProvider>
  );
}

export default Home;
