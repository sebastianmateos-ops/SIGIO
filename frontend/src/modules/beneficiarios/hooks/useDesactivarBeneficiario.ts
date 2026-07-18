import { useMutation, useQueryClient } from "@tanstack/react-query";

import beneficiarioService from "../services/beneficiarioService";

export function useDesactivarBeneficiario() {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (id: number) =>
      beneficiarioService.eliminar(id),

    onSuccess: () => {
      queryClient.invalidateQueries({
        queryKey: ["beneficiarios"],
      });
    },
  });
}