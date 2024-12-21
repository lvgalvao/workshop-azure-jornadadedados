CREATE TABLE BitcoinData (
    id INT IDENTITY(1,1) PRIMARY KEY,
    valor FLOAT NOT NULL,
    criptomoeda NVARCHAR(10) NOT NULL,
    moeda NVARCHAR(10) NOT NULL,
    timestamp DATETIME NOT NULL
);
