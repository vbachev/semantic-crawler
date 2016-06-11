# Python Semantic Crawler

A simple crawler in python that takes a list of terms as input and fetches structured semantic data for each one from a predefined set of data sources.

## Database usage

`semantic_crawler.py` is the main application script. The list of terms is taken from a MySQL database table (`terms`) and the result of the crawling and analyzing of the data is stored in a different MySQL table (`queries`).

### Schema

To recreate this database schema use the SQL below

```SQL
CREATE DATABASE IF NOT EXISTS `pycrawler` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `pycrawler`;

CREATE TABLE IF NOT EXISTS `queries` (
  `qid` int(8) NOT NULL AUTO_INCREMENT,
  `tid` int(8) NOT NULL,
  `title` varchar(80) NOT NULL,
  `summary` text NOT NULL,
  `categories` text NOT NULL,
  `nouns` text NOT NULL,
  `adjectives` text NOT NULL,
  `updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`qid`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=6 ;

CREATE TABLE IF NOT EXISTS `terms` (
  `tid` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`tid`),
  FULLTEXT KEY `name` (`name`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=8 ;
```

## Command-line interface usage

`semantic_crawler_cli.py` can be used as a CLI application. It will receive search terms as arguments and the resulting JSON data can be piped to other applications.

### Example usage

Command:
```bash
$ python semantic_crawler_cli.py github toroid
```

Output:
```json
{"adjectives": "web-based,graphical,own,open-source,command-line,Web-based,mobile,anthropomorphized,distributed,private,free,largest,such,several,manga,more", "summary": "GitHub is a web-based Git repository hosting service. It offers all of the distributed revision control and source code management (SCM) functionality of Git as well as adding its own features. Unlike Git, which is strictly a command-line tool, GitHub provides a Web-based graphical interface and desktop as well as mobile integration. It also provides access control and several collaboration features such as bug tracking, feature requests, task management, and wikis for every project.\nGitHub offers both plans for private repositories and free accounts, which are usually used to host open-source software projects. As of April 2016, GitHub reports having more than 14 million users and more than 35 million repositories, making it the largest host of source code in the world.\nThe trademark mascot of GitHub is Octocat, an anthropomorphized cat with cephalopod limbs, done in a manga style.", "nouns": "control,Git,features,feature,code,accounts,cephalopod,users,SCM,limbs,GitHub,service,trademark,integration,desktop,access,source,functionality,collaboration,revision,plans,repository,wikis,tool,Octocat,style,task,April,host,management,interface,world,bug,projects,mascot,tracking,repositories,cat,project,requests,software", "categories": "Bug and issue tracking software,Cloud computing providers,Collaborative projects,Community websites,Computing websites,Cross-platform software,Internet properties established in 2008,Project hosting websites,Project management software,South of Market, San Francisco,Technology companies of the United States,Version control", "title": "GitHub"}
{"adjectives": "revolved,toroid,circular,toroidal,hollow", "summary": "In mathematics, a toroid is a surface of revolution with a hole in the middle, like a doughnut. The axis of revolution passes through the hole and so does not intersect the surface. For example when a rectangle is rotated around an axis parallel to one of its edges, then a hollow rectangle-section ring is produced. If the revolved figure is a circle, then the object is called a torus.\nThe term \"toroid\" Is also used to describe a toroidal polyhedron. In this context a toroid need not be circular and may have any number of holes.", "nouns": "polyhedron,revolution,figure,toroid,number,surface,middle,need,ring,doughnut,axis,passes,mathematics,circle,rectangle,object,edges,hole,parallel,term,rectangle-section,torus,holes,context,example", "categories": "Topology,Geometric shapes", "title": "Toroid"}
```

## Dependencies

- MySQLdb
	- https://github.com/farcepest/MySQLdb1
- Wikipedia python library
	- https://github.com/goldsmith/Wikipedia
- Natural Language Processing (NLP) Toolkit
	- http://www.nltk.org/