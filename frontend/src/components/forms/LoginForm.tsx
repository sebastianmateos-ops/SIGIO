import { Button, Stack, TextField } from "@mui/material";
import { zodResolver } from "@hookform/resolvers/zod";
import { AxiosError } from "axios";
import { useNavigate } from "react-router-dom";
import { useForm } from "react-hook-form";

import { useAuth } from "../../contexts/AuthContext";
import {
  loginSchema,
  type LoginFormData,
} from "../../schemas/loginSchema";
import authService from "../../services/authService";

export default function LoginForm() {
  const { login } = useAuth();

  const navigate = useNavigate();

  const {
    register,
    handleSubmit,
    setError,
    formState: {
      errors,
      isSubmitting,
    },
  } = useForm<LoginFormData>({
    resolver: zodResolver(loginSchema),
    defaultValues: {
      usuario: "",
      password: "",
    },
  });

  async function onSubmit(data: LoginFormData) {
    try {
      const response = await authService.login(data);

      login(response.access_token);

      console.log("JWT recibido:");
      console.log(response);

      navigate("/dashboard", {
      replace: true,
    });

    } catch (error) {
      console.error(error);

      if (error instanceof AxiosError) {
        if (error.response?.status === 401) {
          setError("password", {
            message: "Usuario o contraseña incorrectos.",
          });

          return;
        }
      }

      alert("No fue posible conectar con el servidor.");
    }
  }

  return (
    <Stack
      component="form"
      spacing={2}
      onSubmit={handleSubmit(onSubmit)}
      sx={{
        width: "100%",
      }}
    >
      <TextField
        label="Usuario"
        fullWidth
        autoFocus
        {...register("usuario")}
        error={!!errors.usuario}
        helperText={errors.usuario?.message}
      />

      <TextField
        label="Contraseña"
        type="password"
        fullWidth
        {...register("password")}
        error={!!errors.password}
        helperText={errors.password?.message}
      />

      <Button
        type="submit"
        variant="contained"
        fullWidth
        size="large"
        disabled={isSubmitting}
      >
        {isSubmitting ? "Ingresando..." : "Ingresar"}
      </Button>
    </Stack>
  );
}