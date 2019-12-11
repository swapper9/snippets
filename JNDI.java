//Connecting Spring Boot application (deployed in Websphere Application Server 9) to WAS datasource.

//Connecting to DataSource:

@Bean(name = "WASDataSource")
  public DataSource WASDataSource() throws Exception {        
  JndiDataSourceLookup dataSourceLookup = new JndiDataSourceLookup();
  return dataSourceLookup.getDataSource("java:jdbc/configurationFile");
}   

@Bean(name = "WASDataSourceJdbcTemplate")
  public JdbcTemplate jdbcTemplate_WASDS(@Qualifier("WASDataSource")
  DataSource dsDB2) {
  return new JdbcTemplate(dsDB2);
}

//The name of Datasource is the name which appears on the UI of Websphere console.
//You can see that via -> Select Resources > JDBC > Data Sources.

//jdbc template:
@Autowired
@Qualifier("WASDataSourceJdbcTemplate")
private JdbcTemplate db2WASTemplate;

//And running query using the query method works fine :
db2WASTemplate.query()

//  with tomcat Server.xml:
<GlobalNamingResources>
<Resource auth="Container" driverClassName="com.mysql.jdbc.Driver" 
                           maxActive="20" 
                           maxIdle="0" 
                           maxWait="10000" 
                           name="jdbc/j4s" 
                           password="java4s" 
                           username="java4s"
                           type="javax.sql.DataSource" 
                           url="jdbc:mysql://localhost/test"/>
</GlobalNamingResources>

//context.xml:
<?xml version="1.0" encoding="UTF-8"?>
<context>
	<ResourceLink auth="Container" name="jdbc/j4s" global="jdbc/j4s" type="javax.sql.DataSource" />
</context>

// WebSphere

import com.ibm.websphere.naming.PROPS; // WebSphere naming constants
...
Hashtable env = new Hashtable();
env.put(Context.INITIAL_CONTEXT_FACTORY,
      "com.ibm.websphere.naming.WsnInitialContextFactory");
env.put(Context.PROVIDER_URL, ...);
env.put(PROPS.HOSTNAME_NORMALIZER, PROPS.HOSTNAME_NORMALIZER_NONE);
Context initialContext = new InitialContext(env);
java.lang.Object o = initialContext.lookup(...);
