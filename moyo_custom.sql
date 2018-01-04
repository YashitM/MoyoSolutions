INSERT INTO `socialaccount_socialapp` (`id`, `provider`, `name`, `client_id`, `secret`, `key`) VALUES
(1, 'facebook', 'FacebookApp', '2043167945905470', '898297bb645dfcb1f23878a6e955d106', ''),
(2, 'google', 'GoogleApp', '659267976289-pfhtpi394m8lp0pqredrpp5l0es5sddt.apps.googleusercontent.com', 'fcTj0WOsiqSb2-wdSvuAED4J', '');

INSERT INTO `socialaccount_socialapp_sites` (`id`, `socialapp_id`, `site_id`) VALUES
(1, 1, 1),
(2, 2, 1);

INSERT INTO `django_site` (`id`, `domain`, `name`) VALUES
(1, 'localhost:8000', 'localhost');