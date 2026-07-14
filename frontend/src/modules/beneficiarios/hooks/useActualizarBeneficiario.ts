import { useMutation, useQueryClient } from "@tanstack/react-query";

import beneficiarioService from "../services/beneficiarioService";

export function useActualizarBeneficiario() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: ({
      id,
      datos,
    }: {
      id: number;
      datos: Parameters<
        typeof beneficiarioService.actualizar
      >[1];
    }) =>
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