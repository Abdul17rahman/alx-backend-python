# fixtures.py

from typing import Dict, List

# Define the individual components of your test payload
org_payload: Dict = {"repos_url": "https://api.github.com/orgs/google/repos"}

repos_payload: List[Dict] = [
    {
        "id": 7697149,
        "node_id": "MDEwOlJlcG9zaXRvcnk3Njk3MTQ5",
        "name": "episodes.dart",
        "full_name": "google/episodes.dart",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
            "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
            "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/google",
            "html_url": "https://github.com/google",
            "followers_url": "https://api.github.com/users/google/followers",
            "following_url": "https://api.github.com/users/google/following{/other_user}",
            "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/google/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/google/subscriptions",
            "organizations_url": "https://api.github.com/users/google/orgs",
            "repos_url": "https://api.github.com/users/google/repos",
            "events_url": "https://api.github.com/users/google/events{/privacy}",
            "received_events_url": "https://api.github.com/users/google/received_events",
            "type": "Organization",
            "site_admin": False
        },
        "html_url": "https://github.com/google/episodes.dart",
        "description": "A framework for timing performance of web apps.",
        "fork": False,
        "url": "https://api.github.com/repos/google/episodes.dart",
        "forks_url": "https://api.github.com/repos/google/episodes.dart/forks",
        "keys_url": "https://api.github.com/repos/google/episodes.dart/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/google/episodes.dart/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/google/episodes.dart/teams",
        "hooks_url": "https://api.github.com/repos/google/episodes.dart/hooks",
        "issue_events_url": "https://api.github.com/repos/google/episodes.dart/issues/events{/number}",
        "events_url": "https://api.github.com/repos/google/episodes.dart/events",
        "assignees_url": "https://api.github.com/repos/google/episodes.dart/assignees{/user}",
        "branches_url": "https://api.github.com/repos/google/episodes.dart/branches{/branch}",
        "tags_url": "https://api.github.com/repos/google/episodes.dart/tags",
        "blobs_url": "https://api.github.com/repos/google/episodes.dart/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/google/episodes.dart/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/google/episodes.dart/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/google/episodes.dart/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/google/episodes.dart/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/google/episodes.dart/languages",
        "stargazers_url": "https://api.github.com/repos/google/episodes.dart/stargazers",
        "contributors_url": "https://api.github.com/repos/google/episodes.dart/contributors",
        "subscribers_url": "https://api.github.com/repos/google/episodes.dart/subscribers",
        "subscription_url": "https://api.github.com/repos/google/episodes.dart/subscription",
        "commits_url": "https://api.github.com/repos/google/episodes.dart/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/google/episodes.dart/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/google/episodes.dart/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/google/episodes.dart/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/google/episodes.dart/contents/{+path}",
        "compare_url": "https://api.github.com/repos/google/episodes.dart/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/google/episodes.dart/merges",
        "archive_url": "https://api.github.com/repos/google/episodes.dart/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/google/episodes.dart/downloads",
        "issues_url": "https://api.github.com/repos/google/episodes.dart/issues{/number}",
        "pulls_url": "https://api.github.com/repos/google/episodes.dart/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/google/episodes.dart/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/google/episodes.dart/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/google/episodes.dart/labels{/name}",
        "releases_url": "https://api.github.com/repos/google/episodes.dart/releases{/id}",
        "deployments_url": "https://api.github.com/repos/google/episodes.dart/deployments",
        "created_at": "2013-01-19T00:31:37Z",
        "updated_at": "2019-09-23T11:53:58Z",
        "pushed_at": "2014-10-09T21:39:33Z",
        "git_url": "git://github.com/google/episodes.dart.git",
        "ssh_url": "git@github.com:google/episodes.dart.git",
        "clone_url": "https://github.com/google/episodes.dart.git",
        "svn_url": "https://github.com/google/episodes.dart",
        "homepage": None,
        "size": 191,
        "stargazers_count": 12,
        "watchers_count": 12,
        "language": "Dart",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": False,
        "forks_count": 22,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 0,
        "license": {
            "key": "bsd-3-clause",
            "name": "BSD 3-Clause \"New\" or \"Revised\" License",
            "spdx_id": "BSD-3-Clause",
            "url": "https://api.github.com/licenses/bsd-3-clause",
            "node_id": "MDc6TGljZW5zZTU="
        },
        "forks": 22,
        "open_issues": 0,
        "watchers": 12,
        "default_branch": "master",
        "permissions": {
            "admin": False,
            "push": False,
            "pull": True
        }
    },
    {
        "id": 7776515,
        "node_id": "MDEwOlJlcG9zaXRvcnk3Nzc2NTE1",
        "name": "cpp-netlib",
        "full_name": "google/cpp-netlib",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
            "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
            "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/google",
            "html_url": "https://github.com/google",
            "followers_url": "https://api.github.com/users/google/followers",
            "following_url": "https://api.github.com/users/google/following{/other_user}",
            "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/google/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/google/subscriptions",
            "organizations_url": "https://api.github.com/users/google/orgs",
            "repos_url": "https://api.github.com/users/google/repos",
            "events_url": "https://api.github.com/users/google/events{/privacy}",
            "received_events_url": "https://api.github.com/users/google/received_events",
            "type": "Organization",
            "site_admin": False
        },
        "html_url": "https://github.com/google/cpp-netlib",
        "description": "The C++ Network Library Project -- header-only, cross-platform, standards compliant networking library.",
        "fork": True,
        "url": "https://api.github.com/repos/google/cpp-netlib",
        "forks_url": "https://api.github.com/repos/google/cpp-netlib/forks",
        "keys_url": "https://api.github.com/repos/google/cpp-netlib/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/google/cpp-netlib/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/google/cpp-netlib/teams",
        "hooks_url": "https://api.github.com/repos/google/cpp-netlib/hooks",
        "issue_events_url": "https://api.github.com/repos/google/cpp-netlib/issues/events{/number}",
        "events_url": "https://api.github.com/repos/google/cpp-netlib/events",
        "assignees_url": "https://api.github.com/repos/google/cpp-netlib/assignees{/user}",
        "branches_url": "https://api.github.com/repos/google/cpp-netlib/branches{/branch}",
        "tags_url": "https://api.github.com/repos/google/cpp-netlib/tags",
        "blobs_url": "https://api.github.com/repos/google/cpp-netlib/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/google/cpp-netlib/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/google/cpp-netlib/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/google/cpp-netlib/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/google/cpp-netlib/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/google/cpp-netlib/languages",
        "stargazers_url": "https://api.github.com/repos/google/cpp-netlib/stargazers",
        "contributors_url": "https://api.github.com/repos/google/cpp-netlib/contributors",
        "subscribers_url": "https://api.github.com/repos/google/cpp-netlib/subscribers",
        "subscription_url": "https://api.github.com/repos/google/cpp-netlib/subscription",
        "commits_url": "https://api.github.com/repos/google/cpp-netlib/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/google/cpp-netlib/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/google/cpp-netlib/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/google/cpp-netlib/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/google/cpp-netlib/contents/{+path}",
        "compare_url": "https://api.github.com/repos/google/cpp-netlib/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/google/cpp-netlib/merges",
        "archive_url": "https://api.github.com/repos/google/cpp-netlib/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/google/cpp-netlib/downloads",
        "issues_url": "https://api.github.com/repos/google/cpp-netlib/issues{/number}",
        "pulls_url": "https://api.github.com/repos/google/cpp-netlib/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/google/cpp-netlib/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/google/cpp-netlib/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/google/cpp-netlib/labels{/name}",
        "releases_url": "https://api.github.com/repos/google/cpp-netlib/releases{/id}",
        "deployments_url": "https://api.github.com/repos/google/cpp-netlib/deployments",
        "created_at": "2013-01-23T14:45:32Z",
        "updated_at": "2019-11-15T02:26:31Z",
        "pushed_at": "2018-12-05T17:42:29Z",
        "git_url": "git://github.com/google/cpp-netlib.git",
        "ssh_url": "git@github.com:google/cpp-netlib.git",
        "clone_url": "https://github.com/google/cpp-netlib.git",
        "svn_url": "https://github.com/google/cpp-netlib",
        "homepage": "http://cpp-netlib.github.com/",
        "size": 8937,
        "stargazers_count": 292,
        "watchers_count": 292,
        "language": "C++",
        "has_issues": False,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": False,
        "forks_count": 59,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 0,
        "license": {
            "key": "bsl-1.0",
            "name": "Boost Software License 1.0",
            "spdx_id": "BSL-1.0",
            "url": "https://api.github.com/licenses/bsl-1.0",
            "node_id": "MDc6TGljZW5zZTI4"
        },
        "forks": 59,
        "open_issues": 0,
        "watchers": 292,
        "default_branch": "master",
        "permissions": {
            "admin": False,
            "push": False,
            "pull": True
        }
    },
    {
        "id": 7968417,
        "node_id": "MDEwOlJlcG9zaXRvcnk3OTY4NDE3",
        "name": "dagger",
        "full_name": "google/dagger",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
            "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
            "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/google",
            "html_url": "https://github.com/google",
            "followers_url": "https://api.github.com/users/google/followers",
            "following_url": "https://api.github.com/users/google/following{/other_user}",
            "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/google/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/google/subscriptions",
            "organizations_url": "https://api.github.com/users/google/orgs",
            "repos_url": "https://api.github.com/users/google/repos",
            "events_url": "https://api.github.com/users/google/events{/privacy}",
            "received_events_url": "https://api.github.com/users/google/received_events",
            "type": "Organization",
            "site_admin": False
        },
        "html_url": "https://github.com/google/dagger",
        "description": "A fast dependency injector for Android and Java.",
        "fork": True,
        "url": "https://api.github.com/repos/google/dagger",
        "forks_url": "https://api.github.com/repos/google/dagger/forks",
        "keys_url": "https://api.github.com/repos/google/dagger/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/google/dagger/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/google/dagger/teams",
        "hooks_url": "https://api.github.com/repos/google/dagger/hooks",
        "issue_events_url": "https://api.github.com/repos/google/dagger/issues/events{/number}",
        "events_url": "https://api.github.com/repos/google/dagger/events",
        "assignees_url": "https://api.github.com/repos/google/dagger/assignees{/user}",
        "branches_url": "https://api.github.com/repos/google/dagger/branches{/branch}",
        "tags_url": "https://api.github.com/repos/google/dagger/tags",
        "blobs_url": "https://api.github.com/repos/google/dagger/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/google/dagger/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/google/dagger/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/google/dagger/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/google/dagger/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/google/dagger/languages",
        "stargazers_url": "https://api.github.com/repos/google/dagger/stargazers",
        "contributors_url": "https://api.github.com/repos/google/dagger/contributors",
        "subscribers_url": "https://api.github.com/repos/google/dagger/subscribers",
        "subscription_url": "https://api.github.com/repos/google/dagger/subscription",
        "commits_url": "https://api.github.com/repos/google/dagger/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/google/dagger/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/google/dagger/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/google/dagger/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/google/dagger/contents/{+path}",
        "compare_url": "https://api.github.com/repos/google/dagger/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/google/dagger/merges",
        "archive_url": "https://api.github.com/repos/google/dagger/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/google/dagger/downloads",
        "issues_url": "https://api.github.com/repos/google/dagger/issues{/number}",
        "pulls_url": "https://api.github.com/repos/google/dagger/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/google/dagger/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/google/dagger/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/google/dagger/labels{/name}",
        "releases_url": "https://api.github.com/repos/google/dagger/releases{/id}",
        "deployments_url": "https://api.github.com/repos/google/dagger/deployments",
        "created_at": "2013-02-01T23:14:14Z",
        "updated_at": "2019-12-03T12:39:55Z",
        "pushed_at": "2019-11-27T21:20:38Z",
        "git_url": "git://github.com/google/dagger.git",
        "ssh_url": "git@github.com:google/dagger.git",
        "clone_url": "https://github.com/google/dagger.git",
        "svn_url": "https://github.com/google/dagger",
        "homepage": "https://dagger.dev",
        "size": 59129,
        "stargazers_count": 14492,
        "watchers_count": 14492,
        "language": "Java",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": True,
        "has_pages": True,
        "forks_count": 1741,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 148,
        "license": {
            "key": "apache-2.0",
            "name": "Apache License 2.0",
            "spdx_id": "Apache-2.0",
            "url": "https://api.github.com/licenses/apache-2.0",
            "node_id": "MDc6TGljZW5zZTI="
        },
        "forks": 1741,
        "open_issues": 148,
        "watchers": 14492,
        "default_branch": "master",
        "permissions": {
            "admin": False,
            "push": False,
            "pull": True
        }
    },
    {
        "id": 8165161,
        "node_id": "MDEwOlJlcG9zaXRvcnk4MTY1MTYx",
        "name": "ios-webkit-debug-proxy",
        "full_name": "google/ios-webkit-debug-proxy",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
            "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
            "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/google",
            "html_url": "https://github.com/google",
            "followers_url": "https://api.github.com/users/google/followers",
            "following_url": "https://api.github.com/users/google/following{/other_user}",
            "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/google/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/google/subscriptions",
            "organizations_url": "https://api.github.com/users/google/orgs",
            "repos_url": "https://api.github.com/users/google/repos",
            "events_url": "https://api.github.com/users/google/events{/privacy}",
            "received_events_url": "https://api.github.com/users/google/received_events",
            "type": "Organization",
            "site_admin": False
        },
        "html_url": "https://github.com/google/ios-webkit-debug-proxy",
        "description": "A DevTools proxy (Chrome Remote Debugging Protocol) for iOS devices (Safari Remote Web Inspector).",
        "fork": False,
        "url": "https://api.github.com/repos/google/ios-webkit-debug-proxy",
        "forks_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/forks",
        "keys_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/teams",
        "hooks_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/hooks",
        "issue_events_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/issues/events{/number}",
        "events_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/events",
        "assignees_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/assignees{/user}",
        "branches_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/branches{/branch}",
        "tags_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/tags",
        "blobs_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/languages",
        "stargazers_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/stargazers",
        "contributors_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/contributors",
        "subscribers_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/subscribers",
        "subscription_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/subscription",
        "commits_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/commits{/sha}",
        "git_commits_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/git/commits{/sha}",
        "comments_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/comments{/number}",
        "issue_comment_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/issues/comments{/number}",
        "contents_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/contents/{+path}",
        "compare_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/compare/{base}...{head}",
        "merges_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/merges",
        "archive_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/{archive_format}{/ref}",
        "downloads_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/downloads",
        "issues_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/issues{/number}",
        "pulls_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/pulls{/number}",
        "milestones_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/milestones{/number}",
        "notifications_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/notifications{?since,all,participating}",
        "labels_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/labels{/name}",
        "releases_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/releases{/id}",
        "deployments_url": "https://api.github.com/repos/google/ios-webkit-debug-proxy/deployments",
        "created_at": "2013-02-12T19:08:19Z",
        "updated_at": "2019-12-04T02:06:43Z",
        "pushed_at": "2019-11-24T07:02:13Z",
        "git_url": "git://github.com/google/ios-webkit-debug-proxy.git",
        "ssh_url": "git@github.com:google/ios-webkit-debug-proxy.git",
        "clone_url": "https://github.com/google/ios-webkit-debug-proxy.git",
        "svn_url": "https://github.com/google/ios-webkit-debug-proxy",
        "homepage": "",
        "size": 680,
        "stargazers_count": 4630,
        "watchers_count": 4630,
        "language": "C",
        "has_issues": True,
        "has_projects": True,
        "has_downloads": True,
        "has_wiki": False,
        "has_pages": False,
        "forks_count": 395,
        "mirror_url": None,
        "archived": False,
        "disabled": False,
        "open_issues_count": 24,
        "license": {
            "key": "other",
            "name": "Other",
            "spdx_id": "NOASSERTION",
            "url": None,
            "node_id": "MDc6TGljZW5zZTA="
        },
        "forks": 395,
        "open_issues": 24,
        "watchers": 4630,
        "default_branch": "master",
        "permissions": {
            "admin": False,
            "push": False,
            "pull": True
        }
    },
    {
        "id": 8459994,
        "node_id": "MDEwOlJlcG9zaXRvcnk4NDU5OTk0",
        "name": "google.github.io",
        "full_name": "google/google.github.io",
        "private": False,
        "owner": {
            "login": "google",
            "id": 1342004,
            "node_id": "MDEyOk9yZ2FuaXphdGlvbjEzNDIwMDQ=",
            "avatar_url": "https://avatars1.githubusercontent.com/u/1342004?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/google",
            "html_url": "https://github.com/google",
            "followers_url": "https://api.github.com/users/google/followers",
            "following_url": "https://api.github.com/users/google/following{/other_user}",
            "gists_url": "https://api.github.com/users/google/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/google/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/google/subscriptions",
            "organizations_url": "https://api.github.com/users/google/orgs",
            "repos_url": "https://api.github.com/users/google/repos",
            "events_url": "https://api.github.com/users/google/events{/privacy}",
            "received_events_url": "https://api.github.com/users/google/received_events",
            "type": "Organization",
            "site_admin": False
        },
        "html_url": "https://github.com/google/google.github.io",
        "description": None,
        "fork": False,
        "url": "https://api.github.com/repos/google/google.github.io",
        "forks_url": "https://api.github.com/repos/google/google.github.io/forks",
        "keys_url": "https://api.github.com/repos/google/google.github.io/keys{/key_id}",
        "collaborators_url": "https://api.github.com/repos/google/google.github.io/collaborators{/collaborator}",
        "teams_url": "https://api.github.com/repos/google/google.github.io/teams",
        "hooks_url": "https://api.github.com/repos/google/google.github.io/hooks",
        "issue_events_url": "https://api.github.com/repos/google/google.github.io/issues/events{/number}",
        "events_url": "https://api.github.com/repos/google/google.github.io/events",
        "assignees_url": "https://api.github.com/repos/google/google.github.io/assignees{/user}",
        "branches_url": "https://api.github.com/repos/google/google.github.io/branches{/branch}",
        "tags_url": "https://api.github.com/repos/google/google.github.io/tags",
        "blobs_url": "https://api.github.com/repos/google/google.github.io/git/blobs{/sha}",
        "git_tags_url": "https://api.github.com/repos/google/google.github.io/git/tags{/sha}",
        "git_refs_url": "https://api.github.com/repos/google/google.github.io/git/refs{/sha}",
        "trees_url": "https://api.github.com/repos/google/google.github.io/git/trees{/sha}",
        "statuses_url": "https://api.github.com/repos/google/google.github.io/statuses/{sha}",
        "languages_url": "https://api.github.com/repos/google/google.github.io/languages",
        "stargazers_url": "https://api.github.com/repos/google/google.github.io/stargazers",
    }
]

expected_repos: List[str] = [repo["name"] for repo in repos_payload]

apache2_repos: List[str] = [
    repo["name"]
    for repo in repos_payload
    if repo.get("license", {}).get("key") == "apache-2.0"
]
