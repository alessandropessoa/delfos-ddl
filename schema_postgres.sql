-- ==============================================================================
-- DDL POSTGRESQL: GESTÃO DE OBRAS
-- ==============================================================================

CREATE TABLE empresa (
    id_empresa SERIAL NOT NULL,
    cnpj VARCHAR(14) NOT NULL,
    razao_social VARCHAR(100) NOT NULL,
    data_cadastro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT pk_empresa PRIMARY KEY (id_empresa),
    CONSTRAINT uq_emp_cnpj UNIQUE (cnpj)
);

CREATE TABLE obra (
    id_obra SERIAL NOT NULL,
    id_empresa INT NOT NULL,
    nome_obra VARCHAR(150) NOT NULL,
    orcamento_total NUMERIC(15,2),
    status VARCHAR(20) DEFAULT 'EM_PLANEJAMENTO',
    CONSTRAINT pk_obra PRIMARY KEY (id_obra),
    CONSTRAINT fk_obra_empresa FOREIGN KEY (id_empresa) REFERENCES empresa(id_empresa)
);

CREATE TABLE medicao_fisica (
    id_medicao SERIAL NOT NULL,
    id_obra INT NOT NULL,
    ano_referencia INT NOT NULL,
    mes_referencia INT NOT NULL,
    valor_executado NUMERIC(15,2) NOT NULL,
    data_aprovacao TIMESTAMP,
    CONSTRAINT pk_medicao PRIMARY KEY (id_medicao),
    CONSTRAINT fk_medicao_obra FOREIGN KEY (id_obra) REFERENCES obra(id_obra)
);

-- Índices
CREATE INDEX idx_medicao_tempo ON medicao_fisica (ano_referencia, mes_referencia);
CREATE INDEX idx_obra_status ON obra (status);

-- Comentários
COMMENT ON TABLE empresa IS 'Tabela core de cadastro das empreiteiras parceiras.';
COMMENT ON COLUMN empresa.cnpj IS 'CNPJ da empresa sem máscara de formatação.';
COMMENT ON TABLE obra IS 'Projetos de engenharia e obras públicas cadastradas.';
COMMENT ON COLUMN medicao_fisica.ano_referencia IS 'Ano da medição para fins de faturamento e auditoria temporal.';