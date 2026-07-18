import { useQuery } from "@tanstack/react-query";

import beneficiarioService from "../services/beneficiarioService";

export function useBuscarBeneficiarios(
  texto: string,
) {
  return useQuery({
    queryKey: [
      "beneficiarios",
      "buscar",
      texto,
    ],

    queryFn: () =>
      beneficiarioService.buscar(
        texto,
      ),

    enabled:
      texto.trim().length >= 2,
  });
}