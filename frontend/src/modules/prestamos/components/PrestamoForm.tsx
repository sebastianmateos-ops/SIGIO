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
  prestamoSchema,
  type PrestamoFormData,
} from "../schemas/prestamoSchema";

import type { Implemento } from "@/modules/implementos/types/implemento";
import type { Beneficiario } from "@/modules/beneficiarios/types/beneficiario";

interface Props {
  implementos: Implemento[];
  beneficiarios: Beneficiario[];
  onSubmit: (data: PrestamoFormData) => void;
  loading?: boolean;
}

export default function PrestamoForm({
  implementos,
  beneficiarios,
  onSubmit,
  loading = false,
}: Props) {
  const {
    register,
    control,
    handleSubmit,
    formState: { errors },
  } = useForm<PrestamoFormData>({
    resolver: zodResolver(prestamoSchema),
    defaultValues: {
      implemento_id: undefined,
      beneficiario_id: undefined,
      fecha_prestamo: new Date()
        .toISOString()
        .slice(0, 16),
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
        name="implemento_id"
        control={control}
        render={({ field }) => (
          <TextField
            {...field}
            select
            fullWidth
            label="Implemento"
            error={!!errors.implemento_id}
            helperText={errors.implemento_id?.message}
            value={field.value ?? ""}
            onChange={(e) =>
              field.onChange(Number(e.target.value))
            }
          >
            {implementos.map((implemento) => (
              <MenuItem
                key={implemento.id}
                value={implemento.id}
              >
                {implemento.codigo} - {implemento.marca} {implemento.modelo}
              </MenuItem>
            ))}
          </TextField>
        )}
      />

      <Controller
        name="beneficiario_id"
        control={control}
        render={({ field }) => (
          <TextField
            {...field}
            select
            fullWidth
            label="Beneficiario"
            error={!!errors.beneficiario_id}
            helperText={errors.beneficiario_id?.message}
            value={field.value ?? ""}
            onChange={(e) =>
              field.onChange(Number(e.target.value))
            }
          >
            {beneficiarios.map((beneficiario) => (
              <MenuItem
                key={beneficiario.id}
                value={beneficiario.id}
              >
                {beneficiario.codigo} - {beneficiario.nombre} {beneficiario.apellido}
              </MenuItem>
            ))}
          </TextField>
        )}
      />

      <Grid container spacing={2}>
        <Grid size={{ xs: 12 }}>
          <TextField
            fullWidth
            type="datetime-local"
            label="Fecha del préstamo"
            InputLabelProps={{
              shrink: true,
            }}
            {...register("fecha_prestamo")}
            error={!!errors.fecha_prestamo}
            helperText={errors.fecha_prestamo?.message}
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