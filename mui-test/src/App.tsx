import { Box, Typography } from "@mui/material";

export default function App() {
  return (
    <Box
      sx={{
        p: 4,
      }}
    >
      <Typography
        variant="h4"
        sx={{
          fontWeight: "bold",
        }}
      >
        Hola MUI
      </Typography>
    </Box>
  );
}