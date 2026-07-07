import { createTheme } from "@mui/material/styles";

export const theme = createTheme({
  palette: {
    mode: "light",

    primary: {
      main: "#00529B",
      contrastText: "#FFFFFF",
    },

    secondary: {
      main: "#F2A900",
      contrastText: "#FFFFFF",
    },

    background: {
      default: "#F5F7FA",
      paper: "#FFFFFF",
    },

    text: {
      primary: "#1F2937",
      secondary: "#6B7280",
    },

    success: {
      main: "#2E7D32",
    },

    warning: {
      main: "#ED6C02",
    },

    error: {
      main: "#D32F2F",
    },

    info: {
      main: "#0288D1",
    },
  },

  typography: {
    fontFamily: [
      "Roboto",
      "Arial",
      "sans-serif",
    ].join(","),

    h1: {
      fontWeight: 700,
      fontSize: "2.2rem",
    },

    h2: {
      fontWeight: 700,
      fontSize: "1.8rem",
    },

    h3: {
      fontWeight: 600,
      fontSize: "1.5rem",
    },

    h4: {
      fontWeight: 600,
      fontSize: "1.3rem",
    },

    h5: {
      fontWeight: 600,
    },

    h6: {
      fontWeight: 600,
    },

    button: {
      textTransform: "none",
      fontWeight: 600,
    },
  },

  shape: {
    borderRadius: 10,
  },

  components: {
    MuiAppBar: {
      styleOverrides: {
        root: {
          backgroundColor: "#00529B",
        },
      },
    },

    MuiDrawer: {
      styleOverrides: {
        paper: {
          backgroundColor: "#FFFFFF",
        },
      },
    },

    MuiButton: {
      defaultProps: {
        variant: "contained",
      },

      styleOverrides: {
        root: {
          borderRadius: 8,
          boxShadow: "none",

          "&:hover": {
            boxShadow: "0 4px 10px rgba(0,0,0,0.15)",
          },
        },
      },
    },

    MuiCard: {
      styleOverrides: {
        root: {
          borderRadius: 12,
          boxShadow: "0 2px 8px rgba(0,0,0,0.08)",
        },
      },
    },

    MuiPaper: {
      styleOverrides: {
        root: {
          borderRadius: 10,
        },
      },
    },
  },
});