--------------------------------------------------------------------------------
-- View on Sites
CREATE VIEW VAllSites AS
    SELECT iris_grid.Sites.name AS name, 'Grid' AS tag
    FROM iris_grid.Sites
    UNION
    SELECT iris_cloud.Sites.name AS name, 'Cloud' AS tag
    FROM iris_cloud.Sites WHERE (iris_cloud.Sites.name <> 'None');

--------------------------------------------------------------------------------
-- View on VOs

CREATE VIEW VAllVOs AS
    SELECT iris_grid.VOs.name AS name, 'Grid' AS tag
    FROM iris_grid.VOs
    UNION
    SELECT iris_cloud.VOs.name AS name, 'Cloud' AS tag
    FROM iris_cloud.VOs;
