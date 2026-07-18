import {
  Grid,
  MenuItem,
  TextField,
} from "@mui/material";

import { useFormContext } from "react-hook-form";

import type { BeneficiarioFormData } from "../schemas/beneficiarioSchema";

export default function BeneficiarioForm() {
  const {
    register,
    formState: { errors },
  } = useFormContext<BeneficiarioFormData>();

  return (
    <Grid
      container
      spacing={2}
      sx={{ mt: 1 }}
    >
      <Grid size={{ xs: 12, md: 4 }}>
        <TextField
          select
          fullWidth
          label="Tipo de documento"
          defaultValue="CI"
          {...register("tipo_documento")}
          error={!!errors.tipo_documento}
          helperText={errors.tipo_documento?.message}
        >
          <MenuItem value="CI">
            Cédula
          </MenuItem>

          <MenuItem value="PAS">
            Pasaporte
          </MenuItem>

          <MenuItem value="OTRO">
            Otro
          </MenuItem>
        </TextField>
      </Grid>

      <Grid size={{ xs: 12, md: 8 }}>
        <TextField
          fullWidth
          label="Número de documento"
          {...register("numero_documento")}
          error={!!errors.numero_documento}
          helperText={errors.numero_documento?.message}
        />
      </Grid>

      <Grid size={{ xs: 12, md: 6 }}>
        <TextField
          fullWidth
          label="Nombre"
          {...register("nombre")}
          error={!!errors.nombre}
          helperText={errors.nombre?.message}
        />
      </Grid>

      <Grid size={{ xs: 12, md: 6 }}>
        <TextField
          fullWidth
          label="Apellido"
          {...register("apellido")}
          error={!!errors.apellido}
          helperText={errors.apellido?.message}
        />
      </Grid>

      <Grid size={{ xs: 12 }}>
        <TextField
          fullWidth
          type="date"
          label="Fecha de nacimiento"
          slotProps={{
            inputLabel: {
              shrink: true,
            },
          }}
          {...register("fecha_nacimiento")}
        />
      </Grid>

      <Grid size={{ xs: 12, md: 6 }}>
        <TextField
          fullWidth
          label="Teléfono"
          {...register("telefono")}
        />
      </Grid>

      <Grid size={{ xs: 12, md: 6 }}>
        <TextField
          fullWidth
          label="Celular"
          {...register("celular")}
        />
      </Grid>

      <Grid size={{ xs: 12 }}>
        <TextField
          fullWidth
          label="Correo electrónico"
          {...register("email")}
          error={!!errors.email}
          helperText={errors.email?.message}
        />
      </Grid>

      <Grid size={{ xs: 12 }}>
        <TextField
          fullWidth
          label="Dirección"
          {...register("direccion")}
        />
      </Grid>

      <Grid size={{ xs: 12, md: 6 }}>
        <TextField
          fullWidth
          label="Ciudad"
          {...register("ciudad")}
        />
      </Grid>

      <Grid size={{ xs: 12, md: 6 }}>
        <TextField
          fullWidth
          label="Departamento"
          {...register("departamento")}
        />
      </Grid>

      <Grid size={{ xs: 12 }}>
        <TextField
          fullWidth
          multiline
          minRows={4}
          label="Observaciones"
          {...register("observaciones")}
        />
      </Grid>
    </Grid>
  );
}