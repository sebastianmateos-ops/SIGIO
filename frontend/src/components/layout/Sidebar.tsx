import {
  Box,
  Divider,
  List,
  ListItemButton,
  ListItemText,
  Paper,
  Typography,
} from "@mui/material";

const menuItems = [
  "Dashboard",
  "Implementos",
  "Beneficiarios",
  "Préstamos",
  "Mantenimientos",
  "Adquisiciones",
  "Bajas",
  "Reportes",
];

export default function Sidebar() {
  return (
    <Paper
      elevation={2}
      sx={{
        width: 260,
        minHeight: "calc(100vh - 120px)",
        borderRadius: 2,
        overflow: "hidden",
      }}
    >
      <Box
        sx={{
          p: 2,
          bgcolor: "primary.main",
          color: "primary.contrastText",
        }}
      >
        <Typography
          variant="h6"
          fontWeight="bold"
        >
          Menú
        </Typography>
      </Box>

      <Divider />

      <List disablePadding>
        {menuItems.map((item) => (
          <ListItemButton key={item}>
            <ListItemText primary={item} />
          </ListItemButton>
        ))}
      </List>
    </Paper>
  );
}