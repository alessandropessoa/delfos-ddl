-- ==============================================================================
-- DDL POSTGRESQL: GESTÃO DE OBRAS
-- ==============================================================================

CREATE TABLE T_a75d07f8 (
    C_835190e8 SERIAL NOT NULL,
    C_9d10d4e4 VARCHAR(14) NOT NULL,
    C_291b360b VARCHAR(100) NOT NULL,
    C_6d1312e8 TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT K_e5a6eda7 PRIMARY KEY (C_835190e8),
    CONSTRAINT K_b69e49ae UNIQUE (C_9d10d4e4)
);

CREATE TABLE T_e2098dbf (
    C_cf4a6e1b SERIAL NOT NULL,
    C_835190e8 INT NOT NULL,
    C_4f8b69bf VARCHAR(150) NOT NULL,
    C_3c1a4c64 NUMERIC(15,2),
    C_8c2e4a03 VARCHAR(20) DEFAULT 'EM_PLANEJAMENTO',
    CONSTRAINT K_060c120c PRIMARY KEY (C_cf4a6e1b),
    CONSTRAINT K_604f6592 FOREIGN KEY (C_835190e8) REFERENCES T_a75d07f8(C_835190e8)
);

CREATE TABLE T_7ee4e828 (
    id_medicao SERIAL NOT NULL,
    C_cf4a6e1b INT NOT NULL,
    C_74507a61 INT NOT NULL,
    C_3e546edb INT NOT NULL,
    C_f02308d1 NUMERIC(15,2) NOT NULL,
    C_3129d9ad TIMESTAMP,
    CONSTRAINT K_a05e7e3d PRIMARY KEY (id_medicao),
    CONSTRAINT K_013e5099 FOREIGN KEY (C_cf4a6e1b) REFERENCES T_e2098dbf(C_cf4a6e1b)
);

-- Índices
CREATE INDEX I_f40c92fe ON T_7ee4e828 (C_74507a61, C_3e546edb);
CREATE INDEX I_ea0675ce ON T_e2098dbf (C_8c2e4a03);

-- Comentários
COMMENT ON TABLE T_a75d07f8 IS 'Tabela core de cadastro das empreiteiras parceiras.';
COMMENT ON COLUMN T_a75d07f8.C_9d10d4e4 IS 'C_9d10d4e4 da T_a75d07f8 sem máscara de formatação.';
COMMENT ON TABLE T_e2098dbf IS 'Projetos de engenharia e obras públicas cadastradas.';
COMMENT ON COLUMN T_7ee4e828.C_74507a61 IS 'Ano da medição para fins de faturamento e auditoria temporal.';