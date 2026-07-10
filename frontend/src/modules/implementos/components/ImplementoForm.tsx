import {
  Button,
  Grid,
  MenuItem,
  Stack,
  TextField,
} from "@mui/material";

import { Controller, useForm } from "react-hook-form";
import { zodResolver } from "@hookform/resolvers/zod";

import {
  implementoSchema,
  type ImplementoFormData,
} from "../schemas/implementoSchema";

import type { Categoria } from "@/modules/catalogos/categorias/types/categoria";


interface Props {
  categorias: Categoria[];
  onSubmit: (data: ImplementoFormData) => void;
  loading?: boolean;
}

export default function ImplementoForm({
  categorias,
  onSubmit,
  loading = false,
}: Props) {
  const {
    register,
    control,
    handleSubmit,
    formState: { errors },
  } = useForm<ImplementoFormData>({
    resolver: zodResolver(implementoSchema),
    defaultValues: {
      categoria_id: undefined,
      marca: "",
      modelo: "",
      numero_serie: "",
      valor_estimado: null,
      ubicacion: "",
      observaciones: "",
    },
  });

  return (
    <Stack
      spacing={3}
      component="form"
      onSubmit={handleSubmit(onSubmit)}
    >
      <Controller
        name="categoria_id"
        control={control}
        render={({ field }) => (
          <TextField
            {...field}
            select
            fullWidth
            label="Categoría"
            error={!!errors.categoria_id}
            helperText={errors.categoria_id?.message}
            value={field.value ?? ""}
            onChange={(e) =>
              field.onChange(Number(e.target.value))
            }
          >
            {categorias.map((categoria) => (
              <MenuItem
                key={categoria.id}
                value={categoria.id}
              >
                {categoria.nombre}
              </MenuItem>
            ))}
          </TextField>
        )}
      />

      <Grid container spacing={2}>
        <Grid size={{ xs: 12, md: 6 }}>
          <TextField
            fullWidth
            label="Marca"
            {...register("marca")}
            error={!!errors.marca}
            helperText={errors.marca?.message}
          />
        </Grid>

        <Grid size={{ xs: 12, md: 6 }}>
          <TextField
            fullWidth
            label="Modelo"
            {...register("modelo")}
            error={!!errors.modelo}
            helperText={errors.modelo?.message}
          />
        </Grid>

        <Grid size={{ xs: 12, md: 6 }}>
          <TextField
            fullWidth
            label="Número de Serie"
            {...register("numero_serie")}
            error={!!errors.numero_serie}
            helperText={errors.numero_serie?.message}
          />
        </Grid>

        <Grid size={{ xs: 12, md: 6 }}>
          <TextField
            fullWidth
            type="number"
            label="Valor Estimado"
            {...register("valor_estimado", {
              setValueAs: (value) =>
                value === "" ? null : Number(value),
            })}
            error={!!errors.valor_estimado}
            helperText={errors.valor_estimado?.message}
          />
        </Grid>

        <Grid size={{ xs: 12 }}>
          <TextField
            fullWidth
            label="Ubicación"
            {...register("ubicacion")}
            error={!!errors.ubicacion}
            helperText={errors.ubicacion?.message}
          />
        </Grid>

        <Grid size={{ xs: 12 }}>
          <TextField
            fullWidth
            multiline
            minRows={4}
            label="Observaciones"
            {...register("observaciones")}
            error={!!errors.observaciones}
            helperText={errors.observaciones?.message}
          />
        </Grid>
      </Grid>

      <Button
        type="submit"
        variant="contained"
        size="large"
        disabled={loading}
      >
        {loading ? "Guardando..." : "Guardar"}
      </Button>
    </Stack>
  );
}