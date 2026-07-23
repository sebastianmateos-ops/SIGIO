import { z } from "zod";

export const prestamoSchema = z.object({
  implemento_id: z
    .number({
      error: "Debe seleccionar un implemento.",
    })
    .int()
    .positive(),

  beneficiario_id: z
    .number({
      error: "Debe seleccionar un beneficiario.",
    })
    .int()
    .positive(),

  fecha_prestamo: z
    .string()
    .min(1, "Debe indicar la fecha del préstamo."),

  observaciones: z
    .string()
    .max(1000, "Máximo 1000 caracteres.")
    .optional(),
});

export type PrestamoFormData =
  z.infer<typeof prestamoSchema>;