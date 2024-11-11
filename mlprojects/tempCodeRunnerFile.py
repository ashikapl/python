sales_state = df.groupby(["State"], as_index=False)["Orders"].sum().sort_values(by="Orders",ascending=False)
# sns.set(rc={"figure.figsize":(10,4)})
# sns.barplot(x="State",y="Orders",data=state_df,color="yellow",saturation=0.6)
# plt.title("Sales_State")
# plt.show()

# print("ACCORDING TO STATE GPRAH")
# print("Note:-> From the above graph we can see that the Uttar-Pradesh and Arunachal-Pradesh are the top most ordering states.")
# print()