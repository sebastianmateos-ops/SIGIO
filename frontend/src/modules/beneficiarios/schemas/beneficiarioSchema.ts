import { z } from "zod";

export const beneficiarioSchema = z.object({
  tipo_documento: z
    .string()
    .min(1, "Seleccione un tipo de documento."),

  numero_documento: z
    .string()
    .trim()
    .min(5, "Documento demasiado corto.")
    .max(20, "Documento demasiado largo."),

  nombre: z
    .string()
    .trim()
    .min(2, "Ingrese el nombre."),

  apellido: z
    .string()
    .trim()
    .min(2, "Ingrese el apellido."),

  fecha_nacimiento: z
    .string()
    .nullable()
    .optional(),

  telefono: z
    .string()
    .trim()
    .nullable()
    .optional(),

  celular: z
    .string()
    .trim()
    .nullable()
    .optional(),

  email: z
    .union([
      z.string().email("Correo electrónico inválido."),
      z.literal(""),
    ])
    .nullable()
    .optional(),

  direccion: z
    .string()
    .trim()
    .nullable()
    .optional(),

  ciudad: z
    .string()
    .trim()
    .nullable()
    .optional(),

  departamento: z
    .string()
    .trim()
    .nullable()
    .optional(),

  observaciones: z
    .string()
    .trim()
    .nullable()
    .optional(),
});

export type BeneficiarioFormData =
  z.infer<typeof beneficiarioSchema>;