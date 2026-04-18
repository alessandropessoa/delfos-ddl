-- ==============================================================================
-- DDL ORACLE: GESTÃO DE OBRAS
-- ==============================================================================

CREATE TABLE T_a75d07f8 (
    C_835190e8 NUMBER(10) NOT NULL,
    C_9d10d4e4 VARCHAR2(14) NOT NULL,
    C_291b360b VARCHAR2(100) NOT NULL,
    C_6d1312e8 DATE DEFAULT SYSDATE,
    CONSTRAINT K_e5a6eda7 PRIMARY KEY (C_835190e8),
    CONSTRAINT K_b69e49ae UNIQUE (C_9d10d4e4)
);

CREATE TABLE T_e2098dbf (
    C_cf4a6e1b NUMBER(10) NOT NULL,
    C_835190e8 NUMBER(10) NOT NULL,
    C_4f8b69bf VARCHAR2(150) NOT NULL,
    C_3c1a4c64 NUMBER(15,2),
    C_8c2e4a03 VARCHAR2(20) DEFAULT 'EM_PLANEJAMENTO',
    CONSTRAINT K_060c120c PRIMARY KEY (C_cf4a6e1b),
    CONSTRAINT K_604f6592 FOREIGN KEY (C_835190e8) REFERENCES T_a75d07f8(C_835190e8)
);

CREATE TABLE T_7ee4e828 (
    C_18aa7f48 NUMBER(10) NOT NULL,
    C_cf4a6e1b NUMBER(10) NOT NULL,
    C_74507a61 NUMBER(4) NOT NULL,
    C_3e546edb NUMBER(2) NOT NULL,
    C_f02308d1 NUMBER(15,2) NOT NULL,
    C_3129d9ad DATE,
    CONSTRAINT K_a05e7e3d PRIMARY KEY (C_18aa7f48),
    CONSTRAINT K_013e5099 FOREIGN KEY (C_cf4a6e1b) REFERENCES T_e2098dbf(C_cf4a6e1b)
);

-- Índices (Testando o peso "idx" do SRE e a identificação de hotspots temporais)
CREATE INDEX I_f40c92fe ON T_7ee4e828 (C_74507a61, C_3e546edb);
CREATE INDEX I_ea0675ce ON T_e2098dbf (C_8c2e4a03);

-- Comentários (Testando o motor de extração de documentação)
COMMENT ON TABLE T_a75d07f8 IS 'Tabela core de cadastro das empreiteiras parceiras.';
COMMENT ON COLUMN T_a75d07f8.C_9d10d4e4 IS 'C_9d10d4e4 da T_a75d07f8 sem máscara de formatação.';
COMMENT ON TABLE T_e2098dbf IS 'Projetos de engenharia e obras públicas cadastradas.';
COMMENT ON COLUMN T_7ee4e828.C_74507a61 IS 'Ano da medição para fins de faturamento e auditoria temporal.';