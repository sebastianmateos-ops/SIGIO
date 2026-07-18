import SearchIcon from "@mui/icons-material/Search";

import {
  InputAdornment,
  TextField,
} from "@mui/material";

interface SearchFieldProps {
  value: string;
  onChange: (value: string) => void;
  placeholder?: string;
  disabled?: boolean;
}

export default function SearchField({
  value,
  onChange,
  placeholder = "Buscar...",
  disabled = false,
}: SearchFieldProps) {
  return (
    <TextField
      fullWidth
      size="small"
      value={value}
      disabled={disabled}
      placeholder={placeholder}
      onChange={(event) =>
        onChange(event.target.value)
      }
      slotProps={{
        input: {
          startAdornment: (
            <InputAdornment position="start">
              <SearchIcon />
            </InputAdornment>
          ),
        },
      }}
    />
  );
}