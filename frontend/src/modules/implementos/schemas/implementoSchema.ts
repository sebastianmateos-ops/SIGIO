import { z } from "zod";

export const implementoSchema = z.object({
  categoria_id: z
    .number({
      error: "Debe seleccionar una categoría.",
    })
    .positive(),

  marca: z
    .string()
    .max(100)
    .optional(),

  modelo: z
    .string()
    .max(100)
    .optional(),

  numero_serie: z
    .string()
    .max(100)
    .optional(),

  valor_estimado: z
    .number()
    .nullable()
    .optional(),

  ubicacion: z
    .string()
    .max(100)
    .optional(),

  observaciones: z
    .string()
    .max(500)
    .optional(),
});

export type ImplementoFormData =
  z.infer<typeof implementoSchema>;