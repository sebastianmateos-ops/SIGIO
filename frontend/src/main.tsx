import React from "react";
import ReactDOM from "react-dom/client";

import { BrowserRouter } from "react-router-dom";

import {
  QueryClient,
  QueryClientProvider,
} from "@tanstack/react-query";

import {
  CssBaseline,
  ThemeProvider,
} from "@mui/material";

import App from "./App";

import { theme } from "./theme/theme";
import { AuthProvider } from "./contexts/AuthContext";

import "./index.css";

const queryClient = new QueryClient();

ReactDOM.createRoot(
  document.getElementById("root") as HTMLElement,
).render(
  <React.StrictMode>
    <ThemeProvider theme={theme}>
      <CssBaseline />

      <QueryClientProvider client={queryClient}>
        <BrowserRouter>
          <AuthProvider>
            <App />
          </AuthProvider>
        </BrowserRouter>
      </QueryClientProvider>

    </ThemeProvider>
  </React.StrictMode>,
);