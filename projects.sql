CREATE TABLE portfolio (
	project_id SERIAL PRIMARY KEY, 
	title VARCHAR(100) NOT NULL,
	project_link VARCHAR(100) NOT NULL,
	images VARCHAR(500) ARRAY NOT NULL
);



INSERT INTO portfolio (title, project_link, images) VALUES('Iris B. Han','https://github.com/ibhan88/web-services','{extra/pexels-anni-roenkae-2457284.jpg, extra/pexels-karolina-grabowska-4046717.jpg, extra/pexels-fauxels-3184460.jpg, extra/pexels-shonejai-1227511.jpg, extra/pexels-steve-johnson-1145720.jpg, extra/pexels-tim-mossholder-1154739.jpg, extra/pexels-mia-von-steinkirch-3894157.jpg, extra/pexels-adrien-olichon-2387532.jpg}');
INSERT INTO portfolio (title, project_link, images) VALUES('My Portfolio Site', 'https://github.com/ibhan88/portfolio-site', '{portfolio/main.png, portfolio/main2.png, portfolio/about.png, portfolio/projects.png, portfolio/project.png, portfolio/skills.png, portfolio/work.png, portfolio/contact.png}');
INSERT INTO portfolio (title, project_link, images) VALUES('Vegan Recipe Collector','https://github.com/ibhan88/My-Vegan-Recipe-Collector','{vegan/screenshot-main.png, vegan/screenshot-register.png, vegan/screenshot-upload-profile.png, vegan/screenshot-login.png, vegan/screenshot-login2.png, vegan/screenshot-search.png, vegan/screenshot-search-results.png, vegan/screenshot-recipe.png, vegan/screenshot-recipe2.png, 
vegan/screenshot-save.png, vegan/screenshot-update-box.png, vegan/screenshot-d3-tree.png}');
INSERT INTO portfolio (title, project_link, images) VALUES('Fourth Project','project_four','{placeholder.jpg, placeholder.jpg, placeholder.jpg, placeholder.jpg, placeholder.jpg, placeholder.jpg}');
INSERT INTO portfolio (title, project_link, images) VALUES('Fifth Project','project_five','{placeholder.jpg, placeholder.jpg, placeholder.jpg, placeholder.jpg, placeholder.jpg, placeholder.jpg}');
INSERT INTO portfolio (title, project_link, images) VALUES('Sixth Project','project_six','{placeholder.jpg, placeholder.jpg, placeholder.jpg, placeholder.jpg, placeholder.jpg, placeholder.jpg}');







