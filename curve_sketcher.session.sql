CREATE TABLE IF NOT EXISTS Functions (
    equation VARCHAR(255) NOT NULL, 
    firstDerivative VARCHAR(255) NOT NULL, 
    secondDerivative VARCHAR(255) NOT NULL, 
    yIntercept DOUBLE NOT NULL,
    roots JSON NOT NULL,
    extrema JSON NOT NULL,
    inflectionPoints JSON NOT NULL,
    verticalAsymptotes JSON NOT NULL,
    horizontalAsymptotes JSON NOT NULL,
    UNIQUE (equation)
);


SELECT * FROM Functions;