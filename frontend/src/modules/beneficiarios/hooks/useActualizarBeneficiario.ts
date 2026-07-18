import { useMutation, useQueryClient } from "@tanstack/react-query";

import beneficiarioService from "../services/beneficiarioService";

import type { BeneficiarioFormData } from "../schemas/beneficiarioSchema";

interface ActualizarBeneficiarioParams {
  id: number;
  datos: BeneficiarioFormData;
}

export function useActualizarBeneficiario() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({
      id,
      datos,
    }: ActualizarBeneficiarioParams) =>
      beneficiarioService.actualizar(
        id,
        datos,
      ),

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["beneficiarios"],
      });
    },
  });
}