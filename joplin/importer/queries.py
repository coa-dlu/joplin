import sys
import re
from string import Template
from gql import gql


# Allows us to use '$$$' as a delimiter for string substitution
class GraphqlParser(Template):
    delimiter="$$$"

fragments = {}

fragments["topiccollection"] = '''
      title
      slug
      description
      liveRevision {
        id
      }
      theme {
        slug
        text
        description
      }
'''

fragments["topic"] = GraphqlParser('''
    title
    slug
    description
    liveRevision {
        id
     }
    topiccollections {
      edges {
        node {
          topiccollection {
              $$$topiccollection
          }
        }
      }
    }
''').substitute(
    topiccollection=fragments["topiccollection"]
)

fragments["contact"] = '''
    id
'''

fragments["information"] = GraphqlParser('''
    title
    slug
    coaGlobal
    description
    additionalContent
    topics {
      edges {
        node {
          topic {
            $$$topic
          }
        }
      }
    }
    contacts {
      edges {
        node {
          contact {
            $$$contact
          }
        }
      }
    }
''').substitute(
    topic=fragments["topic"],
    contact=fragments["contact"],
)

fragments["services"] = GraphqlParser('''
    title
    slug
    coaGlobal
    shortDescription
    steps
    dynamicContent
    additionalContent
    topics {
      edges {
        node {
          topic {
            $$$topic
          }
        }
      }
    }
    contacts {
      edges {
        node {
          contact {
            $$$contact
          }
        }
      }
    }
''').substitute(
    topic=fragments["topic"],
    contact=fragments["contact"],
)

fragments["hours"] = GraphqlParser('''
    mondayStartTime
    mondayEndTime
    mondayStartTime2
    mondayEndTime2
    tuesdayStartTime
    tuesdayEndTime
    tuesdayStartTime2
    tuesdayEndTime2
    wednesdayStartTime
    wednesdayEndTime
    wednesdayStartTime2
    wednesdayEndTime2
    thursdayStartTime
    thursdayEndTime
    thursdayStartTime2
    thursdayEndTime2
    fridayStartTime
    fridayEndTime
    fridayStartTime2
    fridayEndTime2
    saturdayStartTime
    saturdayEndTime
    saturdayStartTime2
    saturdayEndTime2
    sundayStartTime
    sundayEndTime
    sundayStartTime2
    sundayEndTime2
    hoursExceptions
''').substitute(

)

fragments["location"] = GraphqlParser('''
    title
    slug
    coaGlobal
    physicalStreet
    physicalUnit
    physicalCity
    physicalState
    physicalZip
    mailingStreet
    mailingCity
    mailingState
    mailingZip
    phoneNumber
    phoneDescription
    email
    nearestBus1
    nearestBus2
    nearestBus3
    physicalLocationPhoto {
      filename
      title
    }
    $$$hours
''').substitute(
    # relatedServices {
    #   edges {
    #     node {
    #       relatedService {
    #         title
    #       }
    #       hoursSameAsLocation
    #       $$$hours
    #     }
    #   }
    # }
    hours=fragments["hours"],
)

unparsed_query_strings = {
    'topiccollection': '''
        query getTopicCollectionPageRevision($id: ID) {
          allPageRevisions(id: $id) {
            edges {
              node {
                asTopicCollectionPage {
                  $$$topiccollection
                }
              }
            }
          }
        }
    ''',
    'topic': '''
        query getTopicPageRevision($id: ID) {
          allPageRevisions(id: $id) {
            edges {
              node {
                asTopicPage {
                  $$$topic
                }
              }
            }
          }
        }
    ''',
    'information': '''
        query getInformationPageRevision($id: ID) {
          allPageRevisions(id: $id) {
            edges {
              node {
                asInformationPage {
                  $$$information
                }
              }
            }
          }
        }
    ''',
    'services': '''
        query getServicePageRevision($id: ID) {
          allPageRevisions(id: $id) {
            edges {
              node {
                asServicePage {
                  $$$services
                }
              }
            }
          }
        }
    ''',
    'location': '''
    query getLocationPageRevision($id: ID) {
      allPageRevisions(id: $id) {
        edges {
          node {
            asLocationPage {
              $$$location
            }
          }
        }
      }
    }
    ''',
}

query_strings = {
    k: GraphqlParser(v).substitute(**fragments)
    for (k,v) in unparsed_query_strings.items()
}

queries = {
    k: gql(v)
    for (k,v) in query_strings.items()
}


'''
Helper for devs who want to see what each complete query looks like.

Pass query_name to see 1 content type's query:
pipenv run python joplin/importer/queries.py services

Pass no arguments to see all queries:
pipenv run python joplin/importer/queries.py
'''
if __name__ == '__main__':
    # Print query_string with proper indentation
    def pretty_print_graphql(qs):
        # Remove whitespace after newlines
        qs = re.sub(r'(\n)(\s+)', lambda match: '%s' % match.group(1), qs)
        pretty_qs = ""
        indent = 0
        add_spacing = False
        for i in iter(qs):
            if i == "{":
                indent += 1
            if i == "}":
                indent -= 1
            if add_spacing:
                pretty_qs += ("  " * indent)
                add_spacing = False
            if i == "\n":
                add_spacing = True
            pretty_qs += i
        return pretty_qs

    if len(sys.argv) > 1:
        query_name = sys.argv[1]
        qs = query_strings[query_name]
        pretty_qs = pretty_print_graphql(qs)
        print(pretty_qs)
    else:
        for (name, query_string) in query_strings.items():
            print("######")
            print(f"{name}")
            print("######")
            pretty_qs = pretty_print_graphql(query_string)
            print(pretty_qs)
            print("\n")