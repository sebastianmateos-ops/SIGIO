import { Box } from "@mui/material";
import type { ReactNode } from "react";

import Footer from "../components/layout/Footer";
import Header from "../components/layout/Header";
import Sidebar from "../components/layout/Sidebar";

interface MainLayoutProps {
  children: ReactNode;
}

export default function MainLayout({
  children,
}: MainLayoutProps) {
  return (
    <Box
      sx={{
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        bgcolor: "background.default",
      }}
    >
      <Header />

      <Box
        sx={{
          flex: 1,
          display: "flex",
          p: 3,
          gap: 3,
        }}
      >
        <Sidebar />

        <Box
          component="main"
          sx={{
            flex: 1,
          }}
        >
          {children}
        </Box>
      </Box>

      <Footer />
    </Box>
  );
}