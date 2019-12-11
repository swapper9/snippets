//Connecting Spring Boot application (deployed in Websphere Application Server 9) to WAS datasource.

//Connecting to DataSource:

@Bean(name = "WASDataSource")
  public DataSource WASDataSource() throws Exception {        
  JndiDataSourceLookup dataSourceLookup = new JndiDataSourceLookup();
  return dataSourceLookup.getDataSource("DSNAME");
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
